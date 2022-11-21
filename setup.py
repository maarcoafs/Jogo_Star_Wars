import cx_Freeze

executables = [cx_Freeze.Executable(script="StarWars.py",icon="assets/StarWarsIcon.ico")]

cx_Freeze.setup(
 name="Jogo Star Wars",
 options={"build_exe": {"packages":["pygame"],
 "include_files":["assets"]}},
 executables = executables
 ) 