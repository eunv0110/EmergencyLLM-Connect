package com.aivle.mini7.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IntroductionController {
    @GetMapping("/site_introduction")  //
    public String site_introduction() {
        return "site_introduction";

    }
}
