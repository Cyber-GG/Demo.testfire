import { TOTP } from "totp-generator"

// Keys provided must be base32 strings, ie. only containing characters matching (A-Z, 2-7, =).
const { otp } = TOTP.generate("H4VZ46D6FOTECUA2XUAGPFZYAE4BNBYL")

console.log(otp) // prints a 6-digit time-based token based on provided key and current time
