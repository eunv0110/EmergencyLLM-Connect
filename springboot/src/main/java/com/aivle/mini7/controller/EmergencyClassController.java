package com.aivle.mini7.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class EmergencyClassController {
    @GetMapping("/emergency_class")  //
    public String emergency_class() {
        return "emergency_class";
    }
}
