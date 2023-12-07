from pymol import cmd, stored, math

# https://pymolwiki.org/index.php/Load_new_B-factors
def loadBfacts (mol,startaa=1,source="newBfactors.txt", visual="Y"):
    """
    Replaces B-factors with a list of values contained in a plain txt file
    
    usage: loadBfacts mol, [startaa, [source, [visual]]]
 
    mol = any object selection (within one single object though)
    startaa = number of first amino acid in 'new B-factors' file (default=1)
    source = name of the file containing new B-factor values (default=newBfactors.txt)
    visual = redraws structure as cartoon_putty and displays bar with min/max values (default=Y)
 
    example: loadBfacts 1LVM and chain A
    """
    obj=cmd.get_object_list(mol)[0]
    cmd.alter(mol,"b=-1.0")
    inFile = open(source, 'r')
    counter=int(startaa)
    bfacts=[]
    for line in inFile.readlines():    
        bfact=float(line)
        bfacts.append(bfact)
        cmd.alter("%s and resi %s and n. CA"%(mol,counter), "b=%s"%bfact)
        # cmd.alter("%s and resi %s and n. CA"%(mol,counter), "b=%s"%bfact)
        counter=counter+1
    inFile.close()
    if visual=="Y":
        cmd.show_as("cartoon",mol)
        cmd.cartoon("putty", mol)
        cmd.set("cartoon_putty_scale_min", min(bfacts),obj)
        cmd.set("cartoon_putty_scale_max", max(bfacts),obj)
        cmd.set("cartoon_putty_transform", 0,obj)
        cmd.set("cartoon_putty_radius", 0.2,obj)
        cmd.spectrum("b","rainbow", "%s and n. CA " %mol)
        cmd.ramp_new("count", obj, [min(bfacts), max(bfacts)], "rainbow")
        cmd.recolor()

cmd.extend("loadBfacts", loadBfacts)

def main():
    newBfactor_file = "newBfactors.txt"
    
    # datファイルは1行目がRESIDUE, 3行目がcondに対応
    conductivity = []
    with open("input/thermal_cond_intra.dat") as f:
        for line in f:
            conductivity.append(float(line.split()[2]) * 10) # 差を見やすくできると踏んで10倍にしている

    with open(newBfactor_file, "w") as f:
        f.write("\n".join(map(str, conductivity)))

    molecular_name = "dry"
    loadBfacts(molecular_name, source=newBfactor_file, visual="N")

main()
