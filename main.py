import subprocess
import random

class GapFunction():
    def __init__(self, name, statements):
        self.name = name
        self.statements = statements

    def __str__(self):
        statement_literals = "\n    ".join(self.statements)
        return f"""
{self.name} := function()
    {statement_literals}
end;
"""

if __name__ == '__main__':
    rand1 = random.randrange(2, 14, 2)
    rand2 = random.randrange(2, 14, 2)
    statements = [
        "local G, H;",
       f"G := SymmetricGroup({rand1});",
       f"H := SymmetricGroup({rand2});",
      """Print("G: ", G, "\\n");""",
      """Print("H: ", H, "\\n");""",
      """if IsSubgroup(G, H) then
            Print("H is a subgroup of G.\\n");
        else
            Print("H is not a subgroup of G.\\n");
    fi;"""]
    simulation = GapFunction("Simulate", statements)

    with open("simulation.g", "w") as file:
        file.write(str(simulation))

    script_path = './gap_executor.sh'
    subprocess.run(['sh', script_path])