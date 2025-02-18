// Copyright (c) 2025, Demo and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library", {
	refresh(frm) {
     

      // Realtime Chart initialization
      const data = {
        datasets: [
          {
            name: "Some Data",
            values: [],
          },
        ],
      };
  
      // Realtime Chart initialization
      let chart = new frappe.ui.RealtimeChart("#chart", "test_event", 8, {
        title: "My Realtime Chart",
        data: data,
        type: "line",
        height: 250,
        colors: ["#7cd6fd", "#743ee2"],
      });
  
      // Listening to the 'test_event' emitted by the server
      frappe.realtime.on('test_event', function(data) {
        // Assuming `data` received from server looks like this:
        // { label: 1, points: [10] }
  
        // Add the received point to the chart's dataset
        chart.add_data({
          label: data.label,   // Can use the label for the X-axis or any other context
          points: data.points, // Array of points for the Y-axis
        });
      });


      
        },
});
//     frappe.throw(__('This is an Error Message'))
