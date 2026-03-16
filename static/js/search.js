document.addEventListener("DOMContentLoaded", function () {
    // logic for the search feature onto your origin and destination fields
    // We use the IDs Django automatically generates: id_origin and id_destination
    
    if (document.getElementById("id_origin")) {
        new TomSelect("#id_origin", {
            create: false,
            sortField: { field: "text", order: "asc" },
            placeholder: "Search departure city..."
        });
    }

    if (document.getElementById("id_destination")) {
        new TomSelect("#id_destination", {
            create: false,
            sortField: { field: "text", order: "asc" },
            placeholder: "Search arrival city..."
        });
    }
});
