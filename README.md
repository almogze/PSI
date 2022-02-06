# Point Source Interferometer Experiment, Atom-Chip, BGU

![app main page](https://user-images.githubusercontent.com/73799544/152674545-deaf0b2e-a4f3-4eee-b194-1a127044f751.jpg)

This python GUI application developed to the welfare of the PSI experiment team, and to the all colleagues in Atom Chip group.
The application include 3 main parts: 
1)  Pure graphic user interface code which can be found under gui -> uis -> pages. In order to edit those files I used QTdesigner.
2)  Transletion of the code into classes and setup procedures that will enable easier interface between the pages to the rest of the code.
    this can be found at gui -> uis -> windows.
3)  Code that act as application proccess intarface and as can be expected it locate in gui -> uis -> api.

Currently this project consist of 2 workable pages - Atom page and analysis page, a third page is still in progress which will be called fringes page.

## Atom Measurments:
This page analyze the absorption profile of the cloud, and currently can calculate number of atoms and in the futher also temperature of the cloud. Shape of the cloud can be exteact from the Image by moving the vertical and orizontical lines to the center of the cloud.

* Automatic data analysis can calculate simultaneously a sequences of cloud signals ( By pressing "Automatic Pull").  This fitcher configure to work only for bin files with the prefix 'With' and 'Without'.

![atom page - cloud analysis](https://user-images.githubusercontent.com/73799544/152674702-e371646e-231f-4a29-bbd6-9e7116d6a196.jpg)
    
## Analysis Measurments:
A page which can calculate and optimize plots and measurments. I mainly used scipy and iminute in this part. I had a "guess" feature which can set initial parameters to most of the functions. An export to matplotlib figure is enabled as well.
