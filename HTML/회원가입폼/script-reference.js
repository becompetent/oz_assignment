// 폼 요소 선택
const form = document.querySelector('form');

// 사용자 정보 수집 함수
function getUserInfo(formData) {
  const { name, ssn_front, ssn_back, username, password, email, mailbox, address, gender, agree } = formData;
  return {
    name,
    ssn: `${ssn_front}-${ssn_back}`,
    username,
    password,
    email: `${email}@${mailbox}`,
    address,
    gender,
    agree
  };
}

// 유효성 검사 함수
function validateForm({ username, password, passwordRetype }) {
  if (username.length < 4 || username.length > 10) {
    alert('아이디는 4자 이상, 10자 이하로 입력하세요.');
    return false;
  }
  if (password !== passwordRetype) {
    alert('비밀번호가 일치하지 않습니다.');
    return false;
  }
  return true;
}

// 폼 제출 이벤트 리스너 추가
form.addEventListener('submit', function (event) {
  event.preventDefault();// 이벤트가 발생했을 때 부수적으로 일어나는 효과(side effect)
  
  // 폼 데이터 객체 생성
  const formData = {
    name: form.querySelector('#name').value,
    ssn_front: form.querySelector('#ssn_front').value,
    ssn_back: form.querySelector('#ssn_back').value,
    username: form.querySelector('#username').value,
    password: form.querySelector('#password').value,
    passwordRetype: form.querySelector('#password-retype').value,
    email: form.querySelector('#email').value,
    mailbox: form.querySelector('#mailbox').value,
    address: form.querySelector('#address').value,
    gender: form.querySelector('input[name="gender"]:checked')?.value,
    agree: form.querySelector('#agree').checked
  };

  // 유효성 검사 통과 시 결과 출력
  if (validateForm(formData)) {
    const result = getUserInfo(formData);
    console.log(result);
  }
});
