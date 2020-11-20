#!/usr/bin/env bash
rm -rf docs
cd doc-source || exit
rm -rf build
make html
cp -r build/html ../docs/
cd ../
touch docs/.nojekyll
touch .nojekyll
