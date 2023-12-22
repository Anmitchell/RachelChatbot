export const apps = [
  {
    name: 'chatbot-app', // Name of your application process
    script: 'uvicorn', // The script or command to run
    args: [
      'main:app', // Additional arguments for the script
      '--host',
      '0.0.0.0',
      '--port',
      '8000',
      '--workers',
      '4',
    ],
    instances: 1, // Number of instances to run (can be increased for load balancing)
    autorestart: true, // Automatically restart the process if it crashes
    watch: false, // Watch for changes in the source files and restart if necessary
    max_memory_restart: '1G', // Restart the process if its memory usage exceeds the specified limit
  },
  // Add more app configurations if needed
]

/* 
* name: A unique name for your application process managed by PM2. This is used to refer to the process in various PM2 commands.

* script: The script or command to run. In this case, it's "uvicorn" since you're using Uvicorn to run your FastAPI application.

* args: Additional command-line arguments to pass to the script. Here, it specifies the main module (main:app) and some FastAPI-related configuration.

* instances: The number of instances of the script to run. If you want to take advantage of multiple CPU cores, you can increase this value. For example, setting it to 0 means PM2 will spawn as many instances as there are CPU cores.

* autorestart: If set to true, PM2 will automatically restart the process if it crashes. This is useful for ensuring high availability.

* watch: If set to true, PM2 will watch for changes in the source files and restart the process if necessary. This is handy during development but might not be needed in a production environment.

* max_memory_restart: If the process exceeds the specified memory limit, PM2 will restart it. This can help prevent memory leaks from affecting the stability of your application. */
