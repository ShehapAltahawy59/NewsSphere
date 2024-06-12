document.getElementById("search-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    // Get the search query
    var query = document.getElementById("search-input").value.trim();

    // Construct the URL with the search query
    var url = "/search?query=" + encodeURIComponent(query);

    // Redirect the user to the search route
    window.location.href = url;
});
