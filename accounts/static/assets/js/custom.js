const errorMessages = document.querySelectorAll('.error-message');

if (errors) {
  // Loop through each error field
  for (const [field, fieldErrors] of Object.entries(errors)) {
    const errorElement = errorMessages.find(element => element.dataset.field === field);
    
    if (errorElement) {
      // Clear any existing error messages
      errorElement.innerHTML = '';

      // Create a list element to hold error messages
      const errorList = document.createElement('ul');

      // Loop through each error message for the field
      for (const error of fieldErrors) {
        const errorListItem = document.createElement('li');
        errorListItem.textContent = error;
        errorList.appendChild(errorListItem);
      }

      // Add the list of error messages to the error element
      errorElement.appendChild(errorList);
    }
  }
}