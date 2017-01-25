# python-port-scanner

Synopsis

A fast and multithreaded port scanner with GUI that is developed using the tkinter module in python.


Code Example

pslib.py  ---   pslib is te base file that contain methods and a class that runs the port 						scanning (multi-threaded). All you need to import that file and call the methods.

				check_con() 		 --- This method will check the internet connection

				scn_me()    		 --- This method will set the number of ports to scan and 						     throw error if the hostname is blank or internet								 connection is missing.

				popupmessageErr(msg) --- This method throw the error message

				popupmessageInfo(msg)--- This method display the informative message

				run_scn_thread 		 --- This is the class that will run the actual port scanning 						   process. This class methods will be called from the 								 scn_me method so no need to call this class methods from 						   port_scanner file

				START_PORT --- variable will set the port number to start scanning (default = 1)
				END_PORT   --- variable will set the end port to scan (default = 1024)
				TARGET     --- variable stores the host name

tkinter   ---   The tkinter module is used to develop the GUI of the port scanner

socket    ---   The socket module is used for the quering the host at the selected ports by users

threading ---   The threading module is used to double the speed of the port scanner and avoids 
			    freezing of UI while scanning ports.
queue     ---   The queue modue is used to queue the jobs, as job reference to port scanning here
=======
tkinter   ---  The tkinter module is used to develop the GUI of the port scanner<br>
socket    ---  The socket module is used for the quering the host at the selected ports by users<br>
threading ---  The threading module is used to double the speed of the port scanner and avoids 
			   freezing of UI while scanning ports
<br>queue     ---  The queue modue is used to queue the jobs, as job reference to port scanning here
>>>>>>> dfc03e1cd82efa38453f747b3bb727635e3be552


License

MIT License
Copyright (c) 2017 SrceCde

