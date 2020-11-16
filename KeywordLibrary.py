from typing import List, Optional
from TASCommon import TestDetails, AdapterDetails, TestEvidence, Transaction
from winrm import Protocol


class KeywordLibrary:
    
    # Mandatory Parameters used by Keyword functions to return Test Evidence, Action/Step Data, Access the DB
    currentTest = None
    active_step_id = None
    mongo_db = None
    rm = Protocol()

    def __init__(self, mongodb=None, currentTest=None): # Executed Per Test Case doTest  should always have CurrentTest
        # This is called on Instance creation which will occur per Test 
        self.currentTest = currentTest
        self.mongo_db = mongodb

        
    def set_step_id(self,step_id): 
        #This is required to add Results Data to the active step 
        self.active_step_id = step_id 

    def populate_regex(adapter_details, mongo_db): 
        # Function is skipped when parsing, Executed on Adapter Startup 
        
        #Use Common Function to set the specific regex for fields within the Adapter 
        #All other information for the Adapter is gathered directory from the Class Loader 
        #This function is ran automatically after parsing of the class
 
        # Adding a transaction 
        Transaction("adapterStartup", "WINRMAdapter", "INFO", 
                    "Populate Regex for WINRMAdapter", mongo_db) 
 
        adapter_details.set_regex_for_field("alias","^[a-zA-Z0-9]*$")
        adapter_details.set_regex_for_field("hostname","^[a-zA-Z0-9]*$")
        adapter_details.set_regex_for_field("login","^[a-zA-Z0-9]*$")
        adapter_details.set_regex_for_field("password","^[a-zA-Z0-9[$&+,:;=?@#|'<>.-^*()%!]]*$")
        adapter_details.set_regex_for_field("command","^[a-zA-Z0-9[$&+,:;=?@#|'<>.-^*()%!]]*$")
        adapter_details.set_regex_for_field("params","^[a-zA-Z0-9[$&+,:;=?@#|'<>.-^*()%!]]*$")
        adapter_details.set_regex_for_field("script","^[a-zA-Z0-9[$&+,:;=?@#|'<>.-^*()%!]]*$")
        
        
    def winrmadapter_create_session(self, alias, hostname, login, password):
        #Create session with windows host.
        #Does not support domain authentication.
        #*Args:*\n
        #alias_ - robot framework alias to identify the session\n
        #hostname_ -  windows hostname (not IP)\n
        #login_ - windows local login\n
        #password_ - windows local password

        #*Example:*\n
        #| Create Session  |  server  |  windows-host |  Administrator  |  1234567890 |

        session = Protocol(endpoint=hostname,username=login,password=password)


        # This may not be true but use as example
        # Pretend session returns int if successful or null for fail
        if session is uuid:
            return True
        else:
            return False




        
        print ("Performing Create WINRM Session")
        
        Transaction("WINRMExecutionID", self.currentTest.get_WINRM_executionid(), "INFO", 
                    "Performing Create WINRM Session", self.mongo_db)
        
        #Set Results Value in ResultsData           
        self.currentTest.setStepExpectedEvidenceCategory(self.active_step_id, "INFO")
        self.currentTest.setStepExpectedResultData(self.active_step_id, str(result_value)) 
 
        #Set value in global dict
        if results_id in self.results_dict.keys(): 
            self.results_dict[results_id] = result_value 
        else: 
            self.results_dict.update({results_id: result_value}) 
 
        #Last print should flush the stdout buffer to ensure output is seen correctly not needed once trans logging comes 
        print("[" + results_id + "] - Total after operation = " + str(result_value),flush=True) 
 
        return True 

    def winrmadapter_run_cmd(self, alias, command, params) -> winrm.Response:
       
        #Execute command on remote machine.

        #*Args:*\n
        #    _alias_ - robot framework alias to identify the session\n
        #    _command_ -  windows command\n
        #    _params_ - lists of command's parameters

        #Returns:*\n
        #    Result object with methods: status_code, std_out, std_err.

        #*Example:*\n
        #| ${params}=  | Create List  |  "/all" |
        #| ${result}=  |  Run cmd  |  server  |  ipconfig  |  ${params} |
        #| Log  |  ${result.status_code} |
        #| Log  |  ${result.std_out} |
        #| Log  |  ${result.std_err} |
        #=>\n
        #| 0
        #| Windows IP Configuration
        #|    Host Name . . . . . . . . . . . . : WINDOWS-HOST
        #|    Primary Dns Suffix  . . . . . . . :
        #|    Node Type . . . . . . . . . . . . : Hybrid
        #|    IP Routing Enabled. . . . . . . . : No
        #|    WINS Proxy Enabled. . . . . . . . : No
        
        print ("Performing WINRM Run Commmand")
        
        Transaction("WINRMExecutionID", self.currentTest.get_WINRM_executionid(), "INFO", 
                    "Performing WINRM Run Commmand", self.mongo_db)

        if params is not None:
            log_cmd = f'{command} {" ".join(params)}'
        else:
            log_cmd = command
        logger.info(f'Run command on server with alias "{alias}": {log_cmd}')
        self._session = self._cache.switch(alias)
        result = self._session.run_cmd(command, params)
        return result

    def winrmadapter_run_ps(self, alias, script) -> winrm.Response:
        
        #Run power shell script on remote machine.

        #*Args:*\n
        #     _alias_ - robot framework alias to identify the session\n
        #     _script_ -  power shell script\n

        #*Returns:*\n
        #     Result object with methods: status_code, std_out, std_err.

        #*Example:*\n
        #| ${result}=  |  Run ps  |  server  |  get-process iexplore|select -exp ws|measure-object -sum|select -exp Sum |
        #| Log  |  ${result.status_code} |
        #| Log  |  ${result.std_out} |
        #| Log  |  ${result.std_err} |
        # =>\n
        #| 0
        #| 56987648

        logger.info(f'Run power shell script on server with alias "{alias}": {script}')
        self._session = self._cache.switch(alias)
        result = self._session.run_ps(script)
        return result
        
