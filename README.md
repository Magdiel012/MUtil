# MBase

MBase is a ZScript library that attempts to provide a highly-flexible foundation for
GZDoom mods, including a robust state machine implementation to manage complex logic
and a generic system for displaying UI elements without custom status bars, among
other utilities.

## Setup

### ZScript Includes

First, bring the MBaseLib folder into the root of your project archive or directory.

![Example directory structure](doc/setup-1.png)

Then include the main ZScript file from the library.
```c
#include "MBaseLib/zscript.zs"
```
This file will `#include` all other ZScript files contained in the library. Be sure
to place this directive above any `#include`s that may extend classes from MBase.

### Miscellaneous Edits

You will need to make edits to certain lumps in your project, or add them if missing:

##### MAPINFO

You will need to add the `HUDExtensionRegistry` event handler in the `GameInfo` block.
This is needed for the HUD extension system to function.
```cs
GameInfo
{
	AddEventHandlers = "HUDExtensionRegistry"
}
```
> If starting a new project, you may use the premade files in the `setuptemplate`
> folder instead.

### Optional Setup

#### RPLCA0.png

The `WeaponBase` actor uses the RPLC sprite for states that are meant to be replaced
by deriving actors supplying their own sprite, as a visual reminder that the sprite
needs to be replaced:

![Replace Me image](extra/sprites/RPLCA0.png)

Although `WeaponBase` remains fully-functional without it, you are encouraged to
import this sprite to avoid these states appearing blank, which may be misinterpreted
as an unrelated bug during development. You will find it in `extra/sprites/`.
