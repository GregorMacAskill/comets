import cx_Freeze


if False:
    import pygame._view
    
executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "Comets",
    options = {"build_exe": {"packages":["pygame"],
                             "include_files":[r"C:\Users\Gregor\Desktop\USB\AH Computing Project\Comets\img",
                                              r"C:\Users\Gregor\Desktop\USB\AH Computing Project\Comets\sound"]}},
    executables = executables

    )

