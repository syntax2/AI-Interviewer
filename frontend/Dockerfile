

# Serve the frontend using a lightweight HTTP server
# CMD ["npx", "serve", "-s", "build"]
# frontend/Dockerfile

# Use Node.js as base image
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your application code
COPY . .

# Expose port for React app (default is 3000)
EXPOSE 3000

# # Start the application
CMD ["npm", "start"]
# CMD ["npx", "serve", "-s", "build"]