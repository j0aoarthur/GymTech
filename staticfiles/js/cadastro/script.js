const cepInput = document.getElementById("cep");
const error_message = document.getElementById("cepError")

function clearAddressFields() {
  document.getElementById("street").value = '';
  document.getElementById("neighborhood").value = '';
  document.getElementById("city").value = '';
  document.getElementById("state").value = '';
}

function searchCEP() {
  const cep = cepInput.value.replace(/\D/g, ''); // Remove non-numeric characters

  if (cep === '' || !/^\d{8}$/.test(cep)) {
    clearAddressFields();
    error_message.style.display = "block";
    return;
  }

  fetch(`https://viacep.com.br/ws/${cep}/json/`)
    .then(response => response.json())
    .then(data => {
      if (data.erro) {
        clearAddressFields();
        error_message.style.display = "block";


      } else {
        error_message.style.display = "none";
        document.getElementById("street").value = data.logradouro;
        document.getElementById("neighborhood").value = data.bairro;
        document.getElementById("city").value = data.localidade;
        document.getElementById("state").value = data.uf;
      }
    })
    .catch(error => {
      console.error('Error:', error);
      error_message.style.display = "block";
      clearAddressFields();

    });
}

if (cepInput) {
  cepInput.addEventListener("blur", searchCEP);
  cepInput.addEventListener("input", searchCEP);
}

// Mask CPF field
const cpf = document.getElementById("cpf");

if (cpf) {
  cpf.addEventListener('keypress', () => {
    let cpfLength = cpf.value.length

    if (cpfLength === 3 || cpfLength === 7) {
      cpf.value += '.'
    }else if (cpfLength === 11) {
      cpf.value += '-'
    }

  });
}

// Mask Date field
const date = document.getElementById("birthDate")

if (date) {
  date.addEventListener("keypress", () => {
    let dateLength = date.value.length

    if (dateLength === 2 || dateLength == 5) {
      date.value += '/'
    }
  })
}

// Mask Phone field
const phone = document.getElementById("phone")

if (phone) {
  
  phone.addEventListener("keypress", () => {
    let phoneLength = phone.value.length

    switch (phoneLength) {
      case 0:
        phone.value += '('
        break;
      case 3:
        phone.value += ') '
        break;
      case 10:
        phone.value += '-'
    };
  });
};

// Mascarar cep
if (cepInput) {
  cepInput.addEventListener("keypress", () => {
    let cepLength = cepInput.value.length

    if (cepLength === 5) {
      cepInput.value += '-'
    }
  });
};


// Get Due Date
const inputPlan = document.getElementById("plan");

function getDueDate() {
  
  let planName = inputPlan.value;

  // Number of months corresponding the chosen plan
  const planDict = {
    'Mensal': 1,
    'Trimestral': 3,
    'Semestral': 6,
    'Anual': 12,
  };

  let currentDate = new Date();
  let dueDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + planDict[planName], currentDate.getDate());
  let formatedDueDate = dueDate.toLocaleDateString('pt-BR');

  document.getElementById("dueDateLabel").value = formatedDueDate;
}

if (inputPlan) {
  document.addEventListener("DOMContentLoaded", (getDueDate))
  inputPlan.addEventListener("change", (getDueDate))
}


// Preview profile picture
const profileImageDefault = document.getElementById("profileDefault")
  
function preview() {
  profileImageDefault.src = URL.createObjectURL(event.target.files[0]);
}