document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form");
    const userId = document.getElementById("userId");
    const password = document.getElementById("password");
    const pwConfirm = document.getElementById("passwordConfirm");
    const pwStrength = document.getElementById("pwStrength");

    // 아이디 유효성 검사
    userId.addEventListener("input", () => {
        const value = userId.value.trim();
        if (value === "") {
            userId.classList.remove("is-valid", "is-invalid");
            return;
        }
        if (value.length >= 4) {
            userId.classList.add("is-valid");
            userId.classList.remove("is-invalid");
        } else {
            userId.classList.add("is-invalid");
            userId.classList.remove("is-valid");
        }
    });

    // 비밀번호 유효성 검사
    password.addEventListener("input", () => {
        const value = password.value;
        if (value === "") {
            password.classList.remove("is-valid", "is-invalid");
            pwStrength.innerText = "";
            pwConfirm.value = "";
            checkPasswordConfirmValidity();
            return;
        }
        const strong =
            value.length >= 8 &&
            /[0-9]/.test(value) &&
            /[a-zA-Z]/.test(value);
        if (strong) {
            password.classList.add("is-valid");
            password.classList.remove("is-invalid");
            pwStrength.innerText = "✔ 안전한 비밀번호";
            pwStrength.className = "text-success";
        } else {
            password.classList.add("is-invalid");
            password.classList.remove("is-valid");
            pwStrength.innerText = "❌ 8자 이상 + 영문 + 숫자 필요";
            pwStrength.className = "text-danger";
        }
        checkPasswordConfirmValidity();
    });

    // 비밀번호 확인 유효성 검사
    pwConfirm.addEventListener("input", checkPasswordConfirmValidity);

    function checkPasswordConfirmValidity() {
        const confirmValue = pwConfirm.value;
        const passwordValue = password.value;
        if (confirmValue === "") {
            pwConfirm.classList.remove("is-valid", "is-invalid");
            return;
        }
        if (confirmValue === passwordValue && password.classList.contains("is-valid")) {
            pwConfirm.classList.add("is-valid");
            pwConfirm.classList.remove("is-invalid");
        } else {
            pwConfirm.classList.add("is-invalid");
            pwConfirm.classList.remove("is-valid");
        }
    }
document.addEventListener("DOMContentLoaded", () => {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const body = document.body;

    darkModeToggle.addEventListener("click", () => {
        body.classList.toggle("dark-mode");

        // 버튼 텍스트 변경
        if(body.classList.contains("dark-mode")){
            darkModeToggle.textContent = "라이트모드";
        } else {
            darkModeToggle.textContent = "다크모드";
        }
    });
});
// 페이지 로드 시 적용
if(localStorage.getItem("darkMode") === "on"){
    document.body.classList.add("dark-mode");
}

// 버튼 클릭 시 상태 저장
darkModeToggle.addEventListener("click", () => {
    body.classList.toggle("dark-mode");
    if(body.classList.contains("dark-mode")){
        localStorage.setItem("darkMode", "on");
    } else {
        localStorage.setItem("darkMode", "off");
    }
});


    // 폼 제출 이벤트 (가입 버튼 클릭)
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        alert(`${userId.value}님 가입을 축하드립니다! 🎉`);
    });
});
