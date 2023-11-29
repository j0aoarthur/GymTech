'use strict';

document.addEventListener('DOMContentLoaded', function () {

    // ------------------------------------------------------- //
    // Sidebar Functionality
    // ------------------------------------------------------ //
    const sbToggleBtn = document.getElementById('toggle-btn'),
          sideNavbar  = document.querySelector('.side-navbar'),
          innerContent = document.querySelector('.content-inner'),
          smBrand = document.querySelector('.navbar-header .brand-small'),
          lgBrand = document.querySelector('.navbar-header .brand-big');

    if (sideNavbar) {
        sbToggleBtn.addEventListener('click', function (e) {
            e.preventDefault();
            this.classList.toggle('active');

            sideNavbar.classList.toggle('shrinked');
            innerContent.classList.toggle('active');
            document.dispatchEvent(new Event('sidebarChanged'));
        });
    }


    // ------------------------------------------------------- //
    // Material Inputs
    // ------------------------------------------------------ //

    let materialInputs = document.querySelectorAll('input.input-material');
    let materialLabel = document.querySelectorAll('label.label-material');

    // activate labels for prefilled values
    let filledMaterialInputs = Array.from(materialInputs).filter(function (input) {
        return input.value !== '';
    });
    filledMaterialInputs.forEach(input => input.parentElement.lastElementChild.setAttribute('class', 'label-material active'));

    // move label on focus
    materialInputs.forEach((input) => {
        input.addEventListener('focus', function () {
            input.parentElement.lastElementChild.setAttribute('class', 'label-material active');
        });
    });

    // remove/keep label on blur
    materialInputs.forEach((input) => {
        input.addEventListener('blur', function () {
            if (input.value !== '') {
                input.parentElement.lastElementChild.setAttribute('class', 'label-material active');
            } else {
                input.parentElement.lastElementChild.setAttribute('class', 'label-material');
            }
        });
    });


    function bsValidationBehavior(errorInputs, form) {
        function watchError() {
            errorInputs.forEach((input) => {
                if (input.classList.contains('js-validate-error-field')) {
                    input.classList.add('is-invalid');
                    input.classList.remove('is-valid');
                } else {
                    input.classList.remove('is-invalid');
                    input.classList.add('is-valid');
                }
            });
        }
        watchError();
    }


});
