#!/bin/sh
gap -r -b -q << EOI
Read("simulation.g");
Simulate();
EOI