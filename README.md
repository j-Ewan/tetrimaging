a solution to the image hosting problem
upload all the fumens you need to fumens.txt, run the script, commit and push, then in a sheet get the image with =IMAGE("https://raw.githubusercontent.com/j-Ewan/tetrimaging/main/images/"& SUBSTITUTE(SUBSTITUTE(C24,"/","-"),"?","_")&".png",1)
