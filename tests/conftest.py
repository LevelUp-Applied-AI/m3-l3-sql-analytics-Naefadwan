import subprocess
import os

# Save the original subprocess.run function
original_run = subprocess.run

def patched_run(*args, **kwargs):
    """
    Intercept subprocess.run calls. 
    If it spots the hardcoded Unix PATH, it replaces it with your actual Windows PATH.
    """
    if 'env' in kwargs and 'PATH' in kwargs['env']:
        if kwargs['env']['PATH'] == '/usr/bin:/usr/local/bin':
            # Swap out the Unix PATH for your system's real PATH so Windows can find psql
            kwargs['env']['PATH'] = os.environ.get('PATH', '')
            
    return original_run(*args, **kwargs)

# Apply the patch
subprocess.run = patched_run
