import subprocess
import random

class GapSimulation():
    def __init__(self, size1, size2):
        self.size1, self.size2 = size1, size2

    def __str__(self):
        return f"""
Simulate := function()
    local G, H;

    G := SymmetricGroup({self.size1});
    H := SymmetricGroup({self.size2});

    Print("G: ", G, "\\n");
    Print("H: ", H, "\\n");

    if IsSubgroup(G, H) then
        Print("H is a subgroup of G.\\n");
    else
        Print("H is not a subgroup of G.\\n");
    fi;
end;
"""

if __name__ == '__main__':
    rand1 = random.randrange(2, 14, 2)
    rand2 = random.randrange(2, 14, 2)
    simulation = GapSimulation(rand1, rand2);

    with open("simulation.g", "w") as file:
        file.write(str(simulation))

    script_path = './gap_executor.sh'
    subprocess.run(['sh', script_path])