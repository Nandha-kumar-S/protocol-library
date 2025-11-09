# Protocol Library - Deployment Guide

## Production Build

The Protocol Library application has been successfully built for production. The build artifacts are located in the `build/` directory.

### Build Statistics
- **Total Bundle Size**: 350.36 kB (109.06 kB gzipped)
- **CSS Size**: 0.54 kB (0.35 kB gzipped)
- **HTML Size**: 0.46 kB (0.30 kB gzipped)

## Deployment Options

### 1. Static Hosting (Recommended)

The application is a Single Page Application (SPA) and can be deployed to any static hosting service:

#### Netlify
1. **Drag & Drop Deployment**:
   - Go to [netlify.com](https://netlify.com)
   - Drag the `build/` folder to the deployment area
   - Your app will be live instantly

2. **Git-based Deployment**:
   ```bash
   # Connect your repository to Netlify
   # Build command: npm run build
   # Publish directory: build
   ```

#### Vercel
1. **CLI Deployment**:
   ```bash
   npm install -g vercel
   vercel --prod
   ```

2. **Git Integration**:
   - Connect repository to Vercel
   - Auto-deploy on git push

#### GitHub Pages
1. **Setup**:
   ```bash
   npm install --save-dev gh-pages
   ```

2. **Add to package.json**:
   ```json
   {
     "homepage": "https://yourusername.github.io/protocol-library",
     "scripts": {
       "predeploy": "npm run build",
       "deploy": "gh-pages -d build"
     }
   }
   ```

3. **Deploy**:
   ```bash
   npm run deploy
   ```

### 2. Docker Deployment

#### Dockerfile
```dockerfile
# Build stage
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### nginx.conf
```nginx
events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    server {
        listen 80;
        server_name localhost;
        root /usr/share/nginx/html;
        index index.html;

        # Handle client-side routing
        location / {
            try_files $uri $uri/ /index.html;
        }

        # Enable gzip compression
        gzip on;
        gzip_vary on;
        gzip_min_length 1024;
        gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
    }
}
```

#### Build and Run
```bash
docker build -t protocol-library .
docker run -p 80:80 protocol-library
```

### 3. AWS S3 + CloudFront

1. **Create S3 Bucket**:
   ```bash
   aws s3 mb s3://protocol-library-app
   aws s3 sync build/ s3://protocol-library-app
   ```

2. **Configure Static Website Hosting**:
   - Enable static website hosting
   - Set index document: `index.html`
   - Set error document: `index.html` (for SPA routing)

3. **Setup CloudFront Distribution**:
   - Origin: S3 bucket
   - Default root object: `index.html`
   - Error pages: 404 → `/index.html` (200 response)

## Environment Configuration

### Production Environment Variables

Create a `.env.production` file:

```env
# API Configuration
REACT_APP_API_URL=https://your-api-server.com/api
REACT_APP_USE_MOCK_API=false

# Application Settings
REACT_APP_APP_NAME=Protocol Library
REACT_APP_VERSION=1.0.0

# Feature Flags
REACT_APP_ENABLE_FULLSCREEN=true
REACT_APP_ENABLE_EXPORT=true
REACT_APP_ENABLE_THEMES=true

# Production Settings
REACT_APP_DEBUG_MODE=false
REACT_APP_LOG_LEVEL=error
```

### API Integration

To connect to a real backend API:

1. **Update API Configuration**:
   - Set `REACT_APP_USE_MOCK_API=false`
   - Configure `REACT_APP_API_URL` to your API endpoint

2. **API Endpoints Required**:
   ```
   GET    /api/protocols
   POST   /api/protocols
   PUT    /api/protocols/:id
   DELETE /api/protocols/:id
   
   GET    /api/studies
   POST   /api/studies
   PUT    /api/studies/:id
   DELETE /api/studies/:id
   GET    /api/studies/:id/related-pages
   
   GET    /api/jobs
   POST   /api/jobs
   PUT    /api/jobs/:id
   DELETE /api/jobs/:id
   GET    /api/jobs/:id/status
   ```

3. **CORS Configuration**:
   Ensure your API server allows requests from your frontend domain.

## Performance Optimization

### 1. Enable Compression
- Gzip/Brotli compression on server
- Already configured in nginx example above

### 2. Caching Strategy
```nginx
# Cache static assets
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}

# Cache HTML with short expiry
location ~* \.html$ {
    expires 5m;
    add_header Cache-Control "public";
}
```

### 3. CDN Integration
- Use CloudFront, Cloudflare, or similar CDN
- Configure proper cache headers
- Enable compression at CDN level

## Monitoring & Analytics

### 1. Error Tracking
Integrate with services like:
- Sentry
- LogRocket
- Bugsnag

### 2. Performance Monitoring
- Google Analytics
- Mixpanel
- Amplitude

### 3. Uptime Monitoring
- Pingdom
- UptimeRobot
- StatusCake

## Security Considerations

### 1. HTTPS
- Always use HTTPS in production
- Configure HSTS headers
- Use secure cookies if authentication is added

### 2. Content Security Policy
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';">
```

### 3. Environment Variables
- Never commit `.env` files with sensitive data
- Use deployment platform's environment variable features
- Validate all environment variables on startup

## Backup & Recovery

### 1. Code Backup
- Use Git with remote repositories
- Regular automated backups
- Tag releases for easy rollback

### 2. Data Backup
- Regular database backups if using real API
- Export functionality built into the app
- Automated backup schedules

## Maintenance

### 1. Updates
- Regular dependency updates
- Security patch monitoring
- Feature flag management

### 2. Monitoring
- Application performance metrics
- Error rate monitoring
- User experience tracking

## Support

For deployment issues or questions:
1. Check the application logs
2. Verify environment configuration
3. Test API connectivity
4. Review browser console for errors

The Protocol Library is now production-ready with comprehensive deployment options and monitoring capabilities.
