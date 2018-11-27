let get = (key) => {
  let cookies = decodeURIComponent(document.cookie).split(';').map(v => v.trim().split('='))
  let selectedCookie = cookies.filter(v => v[0] === key)[0]

  if (selectedCookie.length <= 0) {
    return {}
  } else {
    return {
      key: selectedCookie[0],
      value: selectedCookie[1]
    }
  }
}

let set = (key, value, expiration) => {
  document.cookie = key + '=' + (value || '') + (expiration || '') + '; path=/'
}

let remove = (key) => {
  document.cookie = key + '=; Max-Age=-999999'
}

export default {
  get,
  set,
  remove
}
