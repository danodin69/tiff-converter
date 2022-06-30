# tiff-converter


If you are ever like me and you get stuck with pip trying to install the GDAL package, here are the steps you can follow to freely use it, and also test the sample code
i have created to convert a tiff file to various extension [pdf, png, jpg ] 

Here We Go!

- Download and Install Anaconda from https://www.anaconda.com/

- Launch Anaconda Navigator after installation is done 

- Go to environments on the sidebar, Click on new at the bottom panel

- a prompt will come up for you to name your environmental and for you to choose your python version, choose the 3.6 version as GDAL breaks on newer versions. 

- Apply it, wait for it to finish downloading.. 

Now there are going to be two environments, base root and yours , make sure yours is selected. 

There's a panel at the top that says 
[Installed ], [channels] , [update index] 

- Click on [installed] and select all  , there's a search bar on that same panel, search for GDAL and select it, then click apply, 


After it installs you should go back to your installed packages dropdown by changing it from [All] to [installed]. You'll see GDAL there. 

Now, go back to home you'll see on the panel, Applications on : [base_root ] 

Make sure it's your new environment that's there and not the base

Then install Spyder IDE from the anaconda navigator! 


Open it and run this code.


# Common Error
Memory Error occurs when the tiff file you are using is too large, it will take up memory in your RAM and fail.

Open an issue on my github if you have problems.
