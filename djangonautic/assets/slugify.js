// grabbing input fields in article_create.html by name
// can get these by inspecting the webpage
const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

// function for slugifying the title
const slugify = (val) => {
    // using regex for replacements
    return val.toString().toLowerCase().trim()
            .replace(/&/g, '-and-') // replacing '&' with '-and-' globally
            .replace(/[\s\W-]+/g, '-') // replaces spaces, non-word chars, and dashes with '-'
};

// adding event listeners
titleInput.addEventListener(type= 'keyup', listener= (e) => {
    // on each keyup, set the value attributee of slugInput to the slugified value of the titleInput
    slugInput.setAttribute('value', slugify(titleInput.value));
});
