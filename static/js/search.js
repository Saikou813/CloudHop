document.addEventListener("DOMContentLoaded", function () {
    // logic for the search feature onto your origin and destination fields
    // We use the IDs Django automatically generates: id_origin and id_destination
    
    document.addEventListener("DOMContentLoaded", function () {
    const settings = {
        create: false,
        sortField: { field: "text", order: "asc" },
        // This tells the box to "blur" (remove focus) after a selection
        onChange: function() {
            this.blur();
        }
    };

    if (document.getElementById("id_origin")) {
        new TomSelect("#id_origin", settings);
    }

    if (document.getElementById("id_destination")) {
        new TomSelect("#id_destination", settings);
    }
});
