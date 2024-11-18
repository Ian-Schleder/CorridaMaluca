# pip install cx_freeze
import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="recursos/icone.ico")
]
cx_Freeze.setup(
    name = "Corrida Maluca",                                                                
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["recursos"]
        }
    }, executables =  executables
)
#python geraSetup.py build || python geraSetup.py bdist_msi
# # build cria apenas acesso '2 cliques', enquanto bdist cria atalho e tudo