import os
import re

def generate_sm_variants():
    # Something else may need the previous working directory, so store it now to reset it later.
    original_wd = os.getcwd()

    os.chdir(os.path.dirname(__file__) + "/../")

    with open("MBaseLib/statemachines/statemachine.zs", encoding="utf-8") as f:
        # Remove all comments and excess newlines.
        base_text = re.sub("\/\/(?![\S]{2,}\.[\w]).*|\/\*(.|\n)+?\*\/", "", f.read())
        base_text = re.sub("\n{2,}|\n\s{2,}\n", "\n", base_text)

    # Generate statemachine_play.zs.
    play_message = """
/*
┌──────────────────────────────────────────────────────────────────────────────┐
│ These are play-scoped versions of the state machine types found in           │
│ statemachines.zs. Please refer to the aforementioned file for documentation. │
└──────────────────────────────────────────────────────────────────────────────┘
*/
"""
    gen_text = "// AUTO-GENERATED\n" + play_message + base_text
    gen_text = re.sub("SMState", "SMStatePlay", gen_text)
    gen_text = re.sub("SMMachine", "SMMachinePlay", gen_text)
    gen_text = re.sub("SMTransition", "SMTransitionPlay", gen_text)
    gen_text = re.sub("class SMStatePlay", "class SMStatePlay play", gen_text, 1)
    gen_text = re.sub("class SMMachinePlay", "class SMMachinePlay play", gen_text, 1)
    gen_text = re.sub("class SMTransitionPlay", "class SMTransitionPlay play", gen_text, 1)

    with open("MBaseLib/statemachines/statemachine_play.zs", "w", encoding="utf-8") as f:
        f.write(gen_text)

    # Generate statemachine_ui.zs.
    ui_message = """
/*
┌──────────────────────────────────────────────────────────────────────────────┐
│ These are UI-scoped versions of the state machine types found in             │
│ statemachines.zs. Please refer to the aforementioned file for documentation. │
└──────────────────────────────────────────────────────────────────────────────┘
*/
"""
    gen_text = "// AUTO-GENERATED\n" + ui_message + base_text
    gen_text = re.sub("SMState", "SMStateUI", gen_text)
    gen_text = re.sub("SMMachine", "SMMachineUI", gen_text)
    gen_text = re.sub("SMTransition", "SMTransitionUI", gen_text)
    gen_text = re.sub("class SMStateUI", "class SMStateUI ui", gen_text, 1)
    gen_text = re.sub("class SMMachineUI", "class SMMachineUI ui", gen_text, 1)
    gen_text = re.sub("class SMTransitionUI", "class SMTransitionUI ui", gen_text, 1)

    with open("MBaseLib/statemachines/statemachine_ui.zs", "w", encoding="utf-8") as f:
        f.write(gen_text)

    os.chdir(original_wd)

def main():
    print("Generating statemachines.zs variants...")
    generate_sm_variants()
    print("Done!")

    print("All tasks complete.")

if __name__ == "__main__":
    main()