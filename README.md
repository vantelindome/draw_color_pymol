# Drawing thermal conductivity in PyMOL

## Process

1. Put input files to ```input/```.

    To the input directory you can put:

    - PDB file of target protein
    - Result of intra-residue thermal conductivity

2. Open ```PyMOL```.

3. In the PyMOL command line type below:

    ```
    cd {current directory}
    load input/dry.pdb
    run draw_intra_tc.py
    spectrum b, blue_white_red
    
    ```