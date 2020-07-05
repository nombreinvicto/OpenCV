// global variable initialisations

let showImageButton = document.getElementById("showImageButton");
let cultureImage = document.getElementById("cultureImage");
let selectImage = document.getElementById("selectImage");
let calculateConfluency = document.getElementById("calculateConfluency");
let calculateConfluencyOutput = document.getElementById("calculated_confluency_op");
let cellTypeOutput = document.getElementById("cell_type_op");
let proliferationHrInput = document.getElementById("proliferation_hr");
let overgrowEstimationButton = document.getElementById("estimateOvergrow");
let overgrowEstimationOutput = document.getElementById("overgrow_estimation_op");
let imagePath = "../static/images/";

// AJAX call handler
function httpRequestHandler(url,
                            body,
                            method,
                            responseObject,
                            makeAsync = true) {
    
    // object and functional initialisations
    let xmlHttp = new XMLHttpRequest();
    
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState === XMLHttpRequest.DONE
            && xmlHttp.status === 200) {
            let responseJSON = JSON.parse(xmlHttp.responseText);
            console.log(responseJSON);
            
        } else if (xmlHttp.status === 500) {
            console.log("Internal server error");
        }
    };
    
    xmlHttp.open(method, url, makeAsync);
    if (method === 'POST') {
        xmlHttp.setRequestHeader("Content-Type",
                                 "application/json;charset=UTF-8");
    }
    
    // finally send the request
    xmlHttp.send(JSON.stringify(body));
    return xmlHttp.responseText; // in case of async request, this
    // line doesnt return anything, probably an unhandled promise
}

// populate drop down list
let fileList = JSON.parse(httpRequestHandler('/populate_select_list',
                                             null,
                                             'GET',
                                             null,
                                             false));
for (let file of fileList) {
    // populate with only jpg files
    let option = document.createElement('option');
    option.text = file;
    selectImage.add(option);
}

// change image
showImageButton.addEventListener("click", () => {
    if (selectImage.value !== "0") {
        cultureImage.src = imagePath + selectImage.value;
    }
});

// calculate confluency
calculateConfluency.addEventListener("click", () => {
    
    let requestBody = {};
    requestBody.fileName = selectImage.value;
    let responseWithConfluencyValue = httpRequestHandler("/calculate_confluency",
                                                         requestBody,
                                                         'POST',
                                                         null,
                                                         false);
    let JSONResponse = JSON.parse(responseWithConfluencyValue);
    let confluency_value = JSONResponse["confluency_value"];
    let cell_type_value = JSONResponse["cell_type"];
    
    calculateConfluencyOutput.innerText = `Calculated Confluency = ${confluency_value} %`;
    cellTypeOutput.innerText = `Cell Type = ${cell_type_value}`;
    
});

overgrowEstimationButton.addEventListener("click", () => {
    let proliferationHour = proliferationHrInput.value;
    let requestBody = {};
    requestBody.proliferationHour = proliferationHour;
    let responseWithOvergrowEstimation = httpRequestHandler("/estimate_overgrow",
                                                            requestBody,
                                                            'POST',
                                                            null,
                                                            false);
    let JSONResponse = JSON.parse(responseWithOvergrowEstimation);
    overgrowEstimationOutput.innerText = JSONResponse["overgrow_estim_text"];
});


