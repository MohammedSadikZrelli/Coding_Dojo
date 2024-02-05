package com.congratz;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/dekashi")
public class DekashiController {
	@RequestMapping("/travel/{country}")
	public String Voyage(@PathVariable("country") String countryID) {
		return "Congratulations you won a travel to " + countryID;
	}
	
	
	
	
	
	 @RequestMapping("/lotto/{moduleId}")
	 public String showLesson(@PathVariable("moduleId") int moduleId){
	    	if (moduleId%2==0) {
	    		return "You will take a grand journey in the near future but be wary of tempting offers";
	    	}	else {
	    			return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends";
	    		}
	    		
	    		
	    	}
	    }


