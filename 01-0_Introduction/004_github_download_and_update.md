# GitHub Course File Management

Git downloads the course files from GitHub. You only need to download the course once. Later, use `git pull` to get new files.

For most students, **HTTPS is the easiest choice**.

## 1. Initial Course Download

Open Terminal. Go to your home folder, then download the course:

```bash
cd ~
git clone https://github.com/sonamu-jun/system-design-and-optimization.git
cd system-design-and-optimization
```

- `cd ~` moves to your home folder.
- `git clone` downloads a new copy of the course.
- `cd system-design-and-optimization` opens the downloaded course folder.

You do not need to run `git clone` again for this course.

## 2. Course File Updates with `git pull`

Open Terminal and move into the course folder:

```bash
cd ~/system-design-and-optimization
git pull
```

Run these two commands when your instructor says that the course files have been updated.

If Git shows a message about files you changed, stop and ask your instructor before continuing. Do not delete your work to remove the message.

More detailed instructions are available in the following videos:
- Pull Requests: [Video Link](https://youtu.be/QlMHQS1Zzro?si=UtG5cx-sAFJNloiz)
- Pull: [Video Link](https://youtu.be/vIqS11aT2I0?si=1NEwrrIYaL0dcsnS)

## 3. Optional SSH Access

SSH is another way to connect Git to GitHub. It needs a special pair of files called an **SSH key**.

- The private key stays on your computer. Never share it.
- The public key ends in `.pub`. You add this key to GitHub.

Use SSH only if you want it or your instructor asks you to use it.

More detailed instructions are available in the following videos:
- SSH Configuration and Cloning: [Video Link](https://youtu.be/Xqla2alRTvc?si=uho8D1JNOfNFfZVe)

### Linux

Open Terminal and run:

```bash
ssh-keygen -t ed25519 -C "your_github_email@example.com"
```

Replace the example email with the email address you use for GitHub. Press Enter to use the suggested file name. Then choose a passphrase and enter it again.

Next, run:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

The last command shows your public key. Copy the whole line.

### Windows with WSL Ubuntu

Open the **Ubuntu** app, not PowerShell, and run the same commands:

```bash
ssh-keygen -t ed25519 -C "your_github_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Use this key only with Git commands that you run in Ubuntu WSL.

### macOS

Open Terminal and run:

```bash
ssh-keygen -t ed25519 -C "your_github_email@example.com"
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

The last command shows your public key. Copy the whole line.

### GitHub Public Key Registration

1. Sign in to GitHub in a web browser.
2. Click your profile picture, then click **Settings**.
3. Click **SSH and GPG keys**, then click **New SSH key**.
4. Give the key a name, paste the public key, and click **Add SSH key**.

Now check the connection in the same terminal:

```bash
ssh -T git@github.com
```

The first time, type `yes` and press Enter if GitHub asks whether to continue.

When the check works, download the course with SSH:

```bash
cd ~
git clone git@github.com:sonamu-jun/system-design-and-optimization.git
cd system-design-and-optimization
```

Use either HTTPS or SSH for one course folder. Do not clone both versions into the same folder.
