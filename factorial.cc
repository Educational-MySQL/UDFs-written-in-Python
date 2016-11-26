#include "python3.5m/Python.h"

int main(int argc, char *argv[])
{
    FILE* file;

    wchar_t **changed_argv;

    changed_argv = (wchar_t**)malloc((argc)*sizeof*changed_argv);

    for (int i = 0; i < argc; i++)
    {
        changed_argv[i] = (wchar_t*)malloc(strlen(argv[i]) + 1);
        mbstowcs(changed_argv[i], argv[i], strlen(argv[i]) + 1);
    }
    printf("%s", changed_argv[0])
    //wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    Py_Initialize();
    Py_SetProgramName(changed_argv[0]);
    PySys_SetArgv(argc, changed_argv);
    file = fopen("factorial.py","r");
    PyRun_SimpleFile(file, "factorial.py");
    Py_Finalize();

    return 0;
}