class LevelUtil play
{
	static play void Explode3D(
		vector3 origin,
		int damage,
		double thrustForce,
		double radius,
		EThrustTarget thrustTarget = THRTARGET_Center,
		array<Actor> exclusions = null,
		Actor source = null,
		Actor inflictor = null,
		vector3 thrustOffset = (0.0, 0.0, 0.0)
		bool checkHit = true)
	{
		let iterator = BlockThingsIterator.CreateFromPos(origin.x, origin.y, origin.z, radius, radius, false);

		while (iterator.Next())
		{
			Actor mo = iterator.thing;

			if (!mo.bSolid || !mo.bShootable) continue;
			if (exclusions && exclusions.Size() > 0 && exclusions.Find(mo) != exclusions.Size()) continue;

			vector3 position;
			switch (thrustTarget)
			{
				case THRTARGET_Center:
					position = (mo.Pos.xy, mo.Pos.z + (mo.Height / 2.0));
					break;
				case THRTARGET_Top:
					position = (mo.Pos.xy, mo.Pos.z + mo.Height);
					break;
				case THRTARGET_Origin:
				default:
					position = mo.Pos;
					break;
			}

			vector3 toTarget = position - origin;
			double distance = toTarget.Length();

			if (distance > radius) continue;

			if (!source) source = WorldAgentHandler.GetWorldAgent();

			vector3 oldPosition = source.Pos;

			source.SetOrigin(origin, false);

			FLineTraceData traceData;
			source.LineTrace(source.AngleTo(mo), radius, ActorUtil.PitchTo(source, mo), data: traceData);

			source.SetOrigin(oldPosition, false);

			if (checkHit && traceData.HitActor != mo) continue;

			int attenuatedDamage = int(round((radius - distance) / radius * damage));
			double attenuatedForce = (radius - distance) / radius * thrustForce;

			mo.DamageMobj(inflictor, source, attenuatedDamage, 'Explosive', DMG_THRUSTLESS | DMG_EXPLOSION);

			ActorUtil.Thrust3D(mo, toTarget + thrustOffset, attenuatedForce);
		}
	}
}

enum EThrustTarget
{
	THRTARGET_Origin,
	THRTARGET_Center,
	THRTARGET_Top
}