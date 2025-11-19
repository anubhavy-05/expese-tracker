// Select the form and inputs
const form = document.getElementById('expense-form');
const nameInput = document.getElementById('expense-name');
const amountInput = document.getElementById('expense-amount');
const dateInput = document.getElementById('expense-date');
// Listen for the form submission
form.addEventListener('submit', addExpense);
// Function to handle adding a new expense
function addExpense(event) {
}
event.preventDefault(); // Stop the page from refreshing
// 1. Get the values from the input fields
const name = nameInput.value.trim();
const amount = amountInput.value;
const date = dateInput.value;