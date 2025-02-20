import { FrappeApp } from 'https://esm.sh/frappe-js-sdk';

const frappe = new FrappeApp('http://192.168.2.127:8007'); 

// Make API call after login
frappe.call()
  .post('librarymanagement.librarymanagement.doctype.library.library.get_city', {
    city_name: "sector 19"
  })
  .then(response => {
    console.log('response', response)
    console.log("Library name is:", response.message);
  })
  .catch(error => console.error("API call error:", error));