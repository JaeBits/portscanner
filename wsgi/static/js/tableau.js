

////////////////////////////////////////////////////////////////////////////////
// Global Variables

var dashboardViz, workbook, activeSheet;

////////////////////////////////////////////////////////////////////////////////
// 1 - Create a View

function initViz(url) {

    var dashboardDiv = document.getElementById("document")
    dashboardURL = url

    var options = {
        hideTabs: true,
        hideToolbar: true,
        onFirstInteractive: function () {

            workbook = dashboardViz.getWorkbook();
            activeSheet = workbook.getActiveSheet();
        }
    };

    dashboardViz = new tableau.Viz(dashboardDiv, dashboardURL, options)
    dashboardViz.addEventListener(tableauSoftware.TableauEventName.MARKS_SELECTION, onMarksSelection);
    
}

////////////////////////////////////////////////////////////////////////////////
// start scripts
$(function (){
    url = $("#url").data("url");
    initViz(url);
});
