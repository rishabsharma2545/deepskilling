# 86. Create a User model with fields: id, email (unique), hashed_password, is_active.

# 87. In a security.py utility file, implement: get_password_hash(password: str) -> str using passlib's 
# CryptContext with bcrypt scheme, and verify_password(plain_password, hashed_password) -> bool.

# 88. Create a POST /api/v1/auth/register/ endpoint that: validates the email format, checks the email is not already registered (return 409 Conflict if so), 
# hashes the password using get_password_hash, and saves the user.

# 89. Never store or log the plain-text password at any point. 
# Add a comment in the code explaining why bcrypt is preferred over MD5 or SHA-256 for passwords.

'''
Passwords are hashed using bcrypt instead of MD5 or SHA-256.
bcrypt is specifically designed for password storage because it
automatically uses a salt and is intentionally slow, making
brute-force and rainbow-table attacks much harder. MD5 and SHA-256
are fast hashing algorithms intended for data integrity, not for
securely storing passwords.
'''

# 90. Test: register a user, then inspect the database — confirm only the hashed password is stored, never the plain text.

'''
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/auth/register/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "gaurav@eduguru.com",
  "password": "123456"
}'

Request URL
http://127.0.0.1:8000/api/v1/auth/register/
	
Response body
{
  "id": 3,
  "email": "gaurav@eduguru.com",
  "is_active": true
}

Response headers
 content-length: 54 
 content-type: application/json 
 date: Sat,04 Jul 2026 19:16:43 GMT 
 location: /api/v1/auth/users/3 
 server: uvicorn 

Successful Response
'''

# 91. Create a POST /api/v1/auth/login/ endpoint that: accepts email and password, verifies credentials using verify_password, 
# creates a JWT token using python-jose with an expiry of 30 minutes, and returns {'access_token': token, 'token_type': 'bearer'}.

# 92. Create a get_current_user(token: str = Depends(oauth2_scheme)) dependency that decodes and validates the JWT token, returning the current user object. 
# Raise 401 if the token is invalid or expired.

# 93. Protect the POST /api/v1/courses/ and DELETE /api/v1/courses/{id}/ endpoints by adding current_user: User = Depends(get_current_user) as a parameter. 
# Unauthenticated requests should receive 401.

# 94. Configure CORS in your app to allow requests from http://localhost:3000 (your frontend dev server). 

# 95. Document in comments: what is the OAuth2 Authorization Code flow, and 
# how does it differ from the simple JWT login you just implemented?

'''
OAuth2 Authorization Code Flow:
1. The user is redirected to an Authorization Server (e.g., Google, GitHub).
2. The user logs in and grants permission to the application.
3. The Authorization Server returns an authorization code.
4. The application exchanges the authorization code for an access token.
5. The access token is then used to access protected resources.

This flow is commonly used for third-party authentication (Single Sign-On)
because the application never sees or stores the user's password.

Simple JWT Login (implemented in this project):
1. The client sends email and password directly to our login endpoint.
2. The server verifies the credentials against the database.
3. If valid, the server generates and returns a JWT access token.
4. The client includes the JWT in the Authorization header
   (Bearer <token>) for subsequent requests.

Key Difference:
- OAuth2 Authorization Code Flow involves an external authorization server
  and authorization code exchange, making it suitable for third-party login.
- Our implementation performs local authentication and directly issues a JWT
  after verifying the user's credentials, making it simpler for a single
  backend application.
'''