document.addEventListener("DOMContentLoaded", function () {
    // 1. Create the settings for the search boxes
    const settings = {
        create: false,
        sortField: { field: "text", order: "asc" },
        // This tells the box to "blur" (remove focus) after a selection
        onChange: function() {
            this.blur();
        }
    };

    // 2. Apply those settings to the 'From' box if it exists
    if (document.getElementById("id_origin")) {
        new TomSelect("#id_origin", settings);
    }

    // 3. Apply those settings to the 'To' box if it exists
    if (document.getElementById("id_destination")) {
        new TomSelect("#id_destination", settings);
    }
});
