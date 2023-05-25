
Simulate := function()
    local G, H;

    G := SymmetricGroup(10);
    H := SymmetricGroup(12);

    Print("G: ", G, "\n");
    Print("H: ", H, "\n");

    if IsSubgroup(G, H) then
        Print("H is a subgroup of G.\n");
    else
        Print("H is not a subgroup of G.\n");
    fi;
end;
