package com.aivle.mini7.controller;

import com.aivle.mini7.client.api.FastApiClient;
import com.aivle.mini7.client.dto.HospitalResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;

@Controller
@RequiredArgsConstructor
@Slf4j
public class IndexController {

    private final FastApiClient fastApiClient;

    @GetMapping("/index")
    public String index() {
        return "index";
    }

    @GetMapping("/recommend_hospital")
    public ModelAndView recommend_hospital(
            @RequestParam("request") String request,
            @RequestParam("latitude") double latitude,
            @RequestParam("longitude") double longitude,
            @RequestParam("hospital_num") int hospitalNum // 추가된 매개변수
    ) {
        // FastApiClient 호출
        List<HospitalResponse> hospitalList = fastApiClient.getHospital(request, latitude, longitude, hospitalNum);
        log.info("hospital: {}", hospitalList);

        ModelAndView mv = new ModelAndView();
        mv.setViewName("recommend_hospital");
        mv.addObject("hospitalList", hospitalList);

        return mv;
    }
}
