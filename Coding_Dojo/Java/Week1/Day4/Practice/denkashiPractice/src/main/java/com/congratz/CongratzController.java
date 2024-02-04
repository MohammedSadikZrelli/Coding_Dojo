package com.congratz;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/")
public class CongratzController {
	@RestController
	@RequestMapping("/daikachi")
	public class HomeController {
	    @RequestMapping("")
	    public String index(){
	      return "Welcome User";
	    }
	    @RequestMapping("/today")
	    public String hello(){
	      return "today u will find luck in all ur endeavors!!";
	    }
	    @RequestMapping("/tomorrow")
	    public String world(){
	      return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
	    }
	}
}