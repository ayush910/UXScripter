# UXScripter
UXS Compiler

This is a compiler for UXS (UX Script).
UXS is a script language for fast prototyping of UI , specifically designed for wrapping build scripts (cmake/nmake etc...).
For example user may select build flavour and bitness and other build criteria using checkboxes and radio buttons, and click a button that will execute the command fabricated using the options.

###Example UXS script:

    RootPosition|pos(0,0)
    OptionSection|pos(10,5,RootPosition)
    ButtonSection|pos(10,50,RootPosition)
    CheckBox(cbBitness)|pos(2,2,OptionSection)|title:"System Archetecture"|["x64","x86"]
    RadioButton(rbDebug)|pos(0,20,cbBitness)|title:"Release or Debug?"|["release","debug"]
    Button(bExec)|pos(0,0,ButtonSection)|title:"Execute"|"cmake build %cbBitness% %rbDebug%"

####This is still under development, will put up full documentation once basic stuff is up and running.
