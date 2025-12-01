
Boss Tracker - Updated (Option C)
================================

What's included:
 - Login system (cookie + JWT)
 - Protected boss tracker (redirects to /login.html if not authenticated)
 - Kill Now button (existing)
 - Set Kill Time modal (frontend + /api/set_kill_time)
 - New API endpoints: /api/login, /api/logout, /api/check_auth, /api/set_kill_time

Deployment notes:
 - Set environment variables on Vercel:
    - MONGO_URI  (your MongoDB Atlas connection)
    - JWT_SECRET (a long secret string)
    - ADMIN_USER (username, default: admin)
    - ADMIN_PASS (password, default: password)

 - The project is compatible with Vercel Python Serverless Functions. Requirements updated in api/requirements.txt.

 - If you already had bosses in MongoDB, the existing structure with 'last_killed' ISO strings will be used.

