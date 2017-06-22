#June2017 Stefano Bosisio
#Setup system for diatomic molecules simulations
#input: nocutoff-constraint; cutoff-constraint
#output:  X_type/
#info: nocutoff-constraint: logP and relative logP for the diatomic mol without constraint and cutoffs
#      cutoff-constraint: what if we add the cutoffperiodic?
#      softcore: what if we modified the soft core potential with shift 0 and 5 ?
#TODO : try to gather everythin in two functions, it's possible!
#Usage: python setup.py nocutoff-constraint/cutoff-constraint/softcore
import os,sys



def nocutoff_constraint():
    #template: inputfiles/constraint/CH~HH/cyclohexane/absolute/allbonds/
    #template out:  X_nocutoff-constraints/relative/CH~HH/run001/cyclohexane/input
    #same for absolute
    #divide between constraint simulation and none constraints

    alldirs = os.listdir(os.getcwd())
    last = 0
    for dirs in alldirs:
        #if a directory starts with a number copy it down
        numb = dirs.split("_")[0]
        try:
            numb = int(numb)
            if numb>last:
                last = numb
        except:
            continue

    last = last+1
    #create the directory
    basedir = "%d_nocutoff_constraint" % last

    if not os.path.exists(basedir):
        os.makedirs(basedir)

    relative = os.path.join(basedir,"relative")
    absolute = os.path.join(basedir,"absolute")
    os.mkdir(relative)
    os.mkdir(absolute)
    #now create CH~HH for relative and HH
    relCH = os.path.join(relative,"CH~HH")
    os.mkdir(relCH)
    relHH = os.path.join(relative,"HH~CH")
    os.mkdir(relHH)
    absCH = os.path.join(absolute,"CH~HH")
    os.mkdir(absCH)
    absHH = os.path.join(absolute,"HH~CH")
    os.mkdir(absHH)
    runs = ["run001","run002","run003"]
    phase = ["cyclohexane","water","vacuum"]
    for run in runs:
        for ph in phase:
            os.makedirs(os.path.join(relCH,run,ph,"input"))
            os.makedirs(os.path.join(relHH,run,ph,"input"))
            os.makedirs(os.path.join(absCH,run,ph,"input"))
            os.makedirs(os.path.join(absHH,run,ph,"input"))

    for run in runs:
        for ph in phase:
            os.makedirs(os.path.join(relCH,run,ph,"output"))
            os.makedirs(os.path.join(relHH,run,ph,"output"))
            os.makedirs(os.path.join(absCH,run,ph,"output"))
            os.makedirs(os.path.join(absHH,run,ph,"output"))
    #TODO maybe gather all this below in a unique function like "copy_inputfiles"
    #now copy all the files
    #inputfiles/constraint/CH~HH/cyclohexane/absolute/noconstraints/
    #CH~HH RELATIVE
    #pass typefolder basedir runs, relCH, absCH, relHH, absHH, phase

    copy_all("nocutoff-constraint",basedir,runs,relCH,absCH,relHH,absHH,phase)

def cutoff_constraint():
    #template: inputfiles/constraint/CH~HH/cyclohexane/absolute/allbonds/
    #template out:  X_nocutoff-constraints/relative/CH~HH/run001/cyclohexane/input
    #same for absolute
    #divide between constraint simulation and none constraints

    alldirs = os.listdir(os.getcwd())
    last = 0
    for dirs in alldirs:
        #if a directory starts with a number copy it down
        numb = dirs.split("_")[0]
        try:
            numb = int(numb)
            if numb>last:
                last = numb
        except:
            continue

    last = last+1
    #create the directory
    basedir = "%d_cutoff_constraint" % last

    if not os.path.exists(basedir):
        os.makedirs(basedir)

    relative = os.path.join(basedir,"relative")
    absolute = os.path.join(basedir,"absolute")
    os.mkdir(relative)
    os.mkdir(absolute)
    #now create CH~HH for relative and HH
    relCH = os.path.join(relative,"CH~HH")
    os.mkdir(relCH)
    relHH = os.path.join(relative,"HH~CH")
    os.mkdir(relHH)
    absCH = os.path.join(absolute,"CH~HH")
    os.mkdir(absCH)
    absHH = os.path.join(absolute,"HH~CH")
    os.mkdir(absHH)
    runs = ["run001","run002","run003"]
    phase = ["cyclohexane","water","vacuum"]
    for run in runs:
        for ph in phase:
            os.makedirs(os.path.join(relCH,run,ph,"input"))
            os.makedirs(os.path.join(relHH,run,ph,"input"))
            os.makedirs(os.path.join(absCH,run,ph,"input"))
            os.makedirs(os.path.join(absHH,run,ph,"input"))

    for run in runs:
        for ph in phase:
            os.makedirs(os.path.join(relCH,run,ph,"output"))
            os.makedirs(os.path.join(relHH,run,ph,"output"))
            os.makedirs(os.path.join(absCH,run,ph,"output"))
            os.makedirs(os.path.join(absHH,run,ph,"output"))
    #TODO maybe gather all this below in a unique function like "copy_inputfiles"
    #now copy all the files
    #inputfiles/constraint/CH~HH/cyclohexane/absolute/noconstraints/
    #CH~HH RELATIVE
    #pass typefolder basedir runs, relCH, absCH, relHH, absHH, phase

    copy_all("cutoff-constraint",basedir,runs,relCH,absCH,relHH,absHH,phase)


def softcore():
    #here as input we have softcore_0 and softcore_5, so you have to call two of them

    alldirs = os.listdir(os.getcwd())
    last = 0
    for dirs in alldirs:
        #if a directory starts with a number copy it down
        numb = dirs.split("_")[0]
        try:
            numb = int(numb)
            if numb>last:
                last = numb
        except:
            continue

    last = last+1
    #create the directory softcore_0
    basedir = "%d_softcore_0" % last

    if not os.path.exists(basedir):
        os.makedirs(basedir)

    relative = os.path.join(basedir,"relative")
    absolute = os.path.join(basedir,"absolute")
    os.mkdir(relative)
    os.mkdir(absolute)
    #now create CH~HH for relative and HH
    relCH = os.path.join(relative,"CH~HH")
    os.mkdir(relCH)
    relHH = os.path.join(relative,"HH~CH")
    os.mkdir(relHH)
    absCH = os.path.join(absolute,"CH~HH")
    os.mkdir(absCH)
    absHH = os.path.join(absolute,"HH~CH")
    os.mkdir(absHH)
    runs = ["run001","run002","run003"]
    phase = ["cyclohexane","water","vacuum"]
    for run in runs:
        for ph in phase:
            os.makedirs(os.path.join(relCH,run,ph,"input"))
            os.makedirs(os.path.join(relHH,run,ph,"input"))
            os.makedirs(os.path.join(absCH,run,ph,"input"))
            os.makedirs(os.path.join(absHH,run,ph,"input"))

    for run in runs:
        for ph in phase:
            os.makedirs(os.path.join(relCH,run,ph,"output"))
            os.makedirs(os.path.join(relHH,run,ph,"output"))
            os.makedirs(os.path.join(absCH,run,ph,"output"))
            os.makedirs(os.path.join(absHH,run,ph,"output"))
    #TODO maybe gather all this below in a unique function like "copy_inputfiles"
    #now copy all the files
    #inputfiles/constraint/CH~HH/cyclohexane/absolute/noconstraints/
    #CH~HH RELATIVE
    #pass typefolder basedir runs, relCH, absCH, relHH, absHH, phase

    copy_all("softcore_0",basedir,runs,relCH,absCH,relHH,absHH,phase)


    #softcore_5

    alldirs = os.listdir(os.getcwd())
    last = 0
    for dirs in alldirs:
        #if a directory starts with a number copy it down
        numb = dirs.split("_")[0]
        try:
            numb = int(numb)
            if numb>last:
                last = numb
        except:
            continue

    last = last+1
    #create the directory softcore_0
    basedir = "%d_softcore_5" % last

    if not os.path.exists(basedir):
        os.makedirs(basedir)

    relative = os.path.join(basedir,"relative")
    absolute = os.path.join(basedir,"absolute")
    os.mkdir(relative)
    os.mkdir(absolute)
    #now create CH~HH for relative and HH
    relCH = os.path.join(relative,"CH~HH")
    os.mkdir(relCH)
    relHH = os.path.join(relative,"HH~CH")
    os.mkdir(relHH)
    absCH = os.path.join(absolute,"CH~HH")
    os.mkdir(absCH)
    absHH = os.path.join(absolute,"HH~CH")
    os.mkdir(absHH)
    runs = ["run001","run002","run003"]
    phase = ["cyclohexane","water","vacuum"]
    for run in runs:
        for ph in phase:
            os.makedirs(os.path.join(relCH,run,ph,"input"))
            os.makedirs(os.path.join(relHH,run,ph,"input"))
            os.makedirs(os.path.join(absCH,run,ph,"input"))
            os.makedirs(os.path.join(absHH,run,ph,"input"))

    for run in runs:
        for ph in phase:
            os.makedirs(os.path.join(relCH,run,ph,"output"))
            os.makedirs(os.path.join(relHH,run,ph,"output"))
            os.makedirs(os.path.join(absCH,run,ph,"output"))
            os.makedirs(os.path.join(absHH,run,ph,"output"))
    #TODO maybe gather all this below in a unique function like "copy_inputfiles"
    #now copy all the files
    #inputfiles/constraint/CH~HH/cyclohexane/absolute/noconstraints/
    #CH~HH RELATIVE
    #pass typefolder basedir runs, relCH, absCH, relHH, absHH, phase

    copy_all("softcore_5",basedir,runs,relCH,absCH,relHH,absHH,phase)

def copy_all(typefolder,basedir,runs,relCH,absCH,relHH,absHH,phase):

    for run in runs:
        for ph in phase:
            directory = os.path.join(relCH,run,ph,"input")

            cmd = "cp inputfiles/%s/CH~HH/%s/relative/noconstraints/* %s/." % (typefolder,ph,directory)
            os.system(cmd)
            print(cmd)
            if ph == "cyclohexane":
                shfile = "cyclo.sh"
            elif ph =="water":
                shfile="water.sh"
            elif ph=="vacuum":
                shfile="vacuum.sh"
            else:
                continue
            dirsh = os.path.join(relCH,run,ph)
            cmd = "cp inputfiles/%s/CH~HH/%s/%s %s/." %(typefolder,ph,shfile,dirsh)
            os.system(cmd)
            print(cmd)
    #HH~CH RELATIVE
    for run in runs:
        for ph in phase:
            directory = os.path.join(relHH,run,ph,"input")

            cmd = "cp inputfiles/%s/HH~CH/%s/relative/noconstraints/* %s/." % (typefolder,ph,directory)
            os.system(cmd)
            print(cmd)
            if ph == "cyclohexane":
                shfile = "cyclo.sh"
            elif ph =="water":
                shfile="water.sh"
            elif ph=="vacuum":
                shfile="vacuum.sh"
            else:
                continue
            dirsh = os.path.join(relHH,run,ph)
            cmd = "cp inputfiles/%s/CH~HH/%s/%s %s/." %(typefolder,ph,shfile,dirsh)
            os.system(cmd)
            print(cmd)
    #CH~HH ABSOLUTE
    for run in runs:
        for ph in phase:
            directory = os.path.join(absCH,run,ph,"input")

            cmd = "cp inputfiles/%s/CH~HH/%s/absolute/noconstraints/* %s/." % (typefolder,ph,directory)
            os.system(cmd)
            print(cmd)
            if ph == "cyclohexane":
                shfile = "cyclo.sh"
            elif ph =="water":
                shfile="water.sh"
            elif ph=="vacuum":
                shfile="vacuum.sh"
            else:
                continue
            dirsh = os.path.join(absCH,run,ph)
            cmd = "cp inputfiles/%s/CH~HH/%s/%s %s/." %(typefolder,ph,shfile,dirsh)
            os.system(cmd)
            print(cmd)
    #HH~CH ABSOLUTE
    for run in runs:
        for ph in phase:
            directory = os.path.join(absHH,run,ph,"input")

            cmd = "cp inputfiles/%s/HH~CH/%s/absolute/noconstraints/* %s/." % (typefolder,ph,directory)
            os.system(cmd)
            print(cmd)
            if ph == "cyclohexane":
                shfile = "cyclo.sh"
            elif ph =="water":
                shfile="water.sh"
            elif ph=="vacuum":
                shfile="vacuum.sh"
            else:
                continue
            dirsh = os.path.join(absHH,run,ph)
            cmd = "cp inputfiles/%s/CH~HH/%s/%s %s/." %(typefolder,ph,shfile,dirsh)
            os.system(cmd)
            print(cmd)








###MAIN###
cmd_sys = sys.argv[1]

if cmd_sys=="nocutoff-constraint":
    #nocutoff-constraints function
    nocutoff_constraint()
    #remember  without () you're not exposing the function
    #output: noctuoff_constraints --> nothing on screen
    #output: nocutoff_constraints() --> last number
elif cmd_sys=="cutoff-constraint":
    #cutoff-constraints function
    cutoff_constraint()
elif cmd_sys=="softcore":
    #softcore function
    softcore()
else:
    print("Please give a correct input:")
    print("nocutoff-constraint, cutoff-constraint, softcore")
    sys.exit(-1)
