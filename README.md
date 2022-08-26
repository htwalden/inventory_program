# README
**MY_CMR program:**
Last updated 24 August 2022 at 1115


**Set Up:**
1. Download the following from the software center:
    - Anaconda 5.3.0 (the icon is a green circle)
	- Follow all installation prompts as applicable.
2. Update the config file. 
    - the name of the file is "config.ini"
    - open "config.ini" in notepad
    - update the three file paths under [FILES] -- only required to update your.name portion
    - example 
        - SOURCE = C:\Users\your.name\source_folder
	    - this is where you will keep all the program files
        -  DESTINATION_REPORT = C:\Users\your.name\source_folder\archive_reports
            - this is where the reconciliation reports will be saved
        -  DESTINATION_IN_PROGRESS = C:\Users\your.name\source_folder\archive_reconciliations
            - this is where the current inventory will be saved, it will be loaded if you choose to                        
          continue a reconciliation from a previously started one. 


**Executing the program:**
1. Open the start menu
2. Search for "Anaconda Prompt"
3. Open Anaconda Prompt
4. A new window will open with a single line:
    (base) C:/
5. Type the following then press ENTER:
    cd C:\Users\your.name\source_folder 
    (this is the same path that contains the program)
6. A second line will appear looking similar to:
    (base) C:\Users\your.name\source_folder
7. Now to run the My_CMR program type and press ENTER:
    python My_CMR.py
8. The program has started and follow the instructions in the command prompt
9. Once all serial numbers are entered type:
    done
10. This will exit the program, save your progress and open up the reconciliation report. 
11. If you are missing inventory and wish to continue the same reconciliation in the future, 
    run the program again following steps 1-7 of this section. 
12. **WARNING** when the program is started the first prompt will ask if this is a new or continued reconciliation. 
                If "n" is entered, indicating a new inventory, the previously saved inventory will be overwritten
                and will need to be manually reloaded from the archives folder. 


Accessing Previous Reports: 
