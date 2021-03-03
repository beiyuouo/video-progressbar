## Help us to help you!

Thank you for taking the time to contribute!

* [Suggesting a feature](#suggesting-a-feature)
* [Filing a bug report](#filing-a-bug-report)
* [Submitting a pull request](#submitting-a-pull-request)

## Suggesting a feature

We can't think of everything. If you've got a good idea for a feature, then please let us know!

Feature suggestions are embraced, but will often be filed for a rainy day. If you require a feature urgently it's best to write it yourself. Don't forget to share ;)

When suggesting a feature, make sure to:

* Check the code on GitHub to make sure it's not already hiding in an unreleased version ;)
* Considered if it's necessary in the library, or is an advanced technique that could be separately explained in an example
* Check existing issues, open and closed, to make sure it hasn't already been suggested

## Filing a bug report

If you're having trouble with our code/libraries/products on your Raspberry Pi try asking on our forums (https://forums.pimoroni.com) or Discord (https://discord.gg/hr93ByC).

If all else fails then please raise an Issue to let us know. Be as detailed as possible, and be ready to answer questions when we get back to you. Make sure you:

* Tell us your model of Raspberry Pi
* Tell us which OS you're using: `lsb_release -d`
* Tell us which Kernel you're running: `uname -a`
* List the steps you've taken so far,
* and any solutions you've tried
* And a paste/picture of the complete output from the failing script/library might help, too!

We have a diagnostic script: `curl get.pimoroni.com/diagnostic | bash` to help you gather information.

## Submitting a pull request

If you've decided to fix a bug, even something as small as a single-letter typo then great! Anything that improves the code/documentation for all future users is warmly welcomed.

If you decide to work on a  requested feature it's best to let us (and everyone else) know what you're working on to avoid any duplication of effort. You can do this by replying to the original Issue for the request.

If you want to contribute an example; go for it! We might not always be able to accept your code, but there's a lot to be learned from trying anyway and if you're new to GitHub we're willing to guide you on that journey.

When contributing a new example or making a change to a library please keep your code style consistent with ours. We try to stick to the pep8 guidelines for Python (https://www.python.org/dev/peps/pep-0008/).

#### Do

* Do use pep8 style guidelines
* Do comment your code where necessary
* Do submit only a single example/feature per pull-request
* Do include a description of what your example is expected to do
* Do add details of your example to examples/README.md if it exists

#### Don't

* Don't include any license information in your examples- our repositories are MIT licensed
* Don't try to do too much at once- submit one or two examples at a time, and be receptive to feedback
* Don't submit multiple variations of the same example, demonstrate one thing concisely

### If you're submitting an example

Try to do one thing, and do it concisely. Keep it simple. Don't mix too many ideas.

The ideal example should:

* demonstrate one idea, technique or API as concisely as possible in a single Python script
* *just work* when you run it. Although sometimes configuration is necessary
* be well commented and attempt to teach the user how and why it works
* document any required configuration, and how to install API keys, dependencies, etc

If you have a more complex example that uses multiple HATs/pHATs or consists of multiple files then consider submitting it as a project instead- either by creating your own GitHub repository and adding the link to the README.md, or by creating a subfolder in the projects/ directory for your code. For example:

* https://github.com/pimoroni/unicorn-hat-hd/tree/master/projects/unicornpaint
* https://github.com/pimoroni/phat-beat/tree/master/projects/vlc-radio

And don't forget to shout about your example on our forums/twitter so we can signal-boost you and let everyone know how awesome you are!

### Licensing

When you submit code to our libraries, you implicitly and irrevocably agree to adopt the associated licenses. You should be able to find this in the file named `LICENSE`.

We typically use the MIT license; which permits Commercial Use, Modification, Distribution and Private use of our code, and therefore also your contributions. It also provides good compatibility with other licenses, and is intended to make re-use of our code as painless as possible for all parties.

You can learn more about the MIT license at Wikipedia: https://en.wikipedia.org/wiki/MIT_License

### Submitting your code

Once you're ready to share your contribution with us you should submit it as a Pull Request.

* Be ready to receive and embrace constructive feedback.
* Be prepared for rejection; we can't always accept contributions. If you're unsure, ask first!

## Thank you!

If you have any questions, concerns or comments about these guidelines, please get in touch. You can do this by raising an issue against our template repository here: https://github.com/pimoroni/template-python

Above all else, we hope you enjoy yourself, learn things and make and share great contributions.

Happy hacking!

-- The Pirate Crew
