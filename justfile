set dotenv-load := false
set shell := ["bash", "-c"]

# Generate components and build the bundle
build:
    rm -r dash_sortable_items
    npm run build
    cp src/python/__init__.py dash_sortable_items
    cp src/python/_imports_.py dash_sortable_items
    cp src/python/SortableItem.py dash_sortable_items
    cp src/python/SortableGroup.py dash_sortable_items
    cp src/python/types.py dash_sortable_items

# Build the webpack bundle
build-js:
    npm run build:js

# Generate the components
generate:
    npm run build:backends

# Rebuild the bundle on change
watch:
    npm run watch

# Install  pip requirements & node modules.
install:
    pip install -r requirements.txt
    npm install

# Package the application for distribution using python wheel.
package: clean build
    python -m build --wheel

# Publish the package to pypi using twine.
publish: package
    twine upload dist/*

# Remove dist & build directories
clean:
    rm -rf dist
    rm -rf build

# Integration testing
test:
    cd test/python && \
    source .venv/bin/activate && \
    pytest --headless

####################################################
#          Documentation related commands          #
####################################################

# Automatically build the docs
build-docs:
    cd docs_src && source .venv/bin/activate && mkdocs build

# Automatically serve the docs
serve-docs:
    cd docs_src && source .venv/bin/activate && mkdocs serve

# Automatically deploy docs
deploy-docs:
    cd docs_src && source .venv/bin/activate && mkdocs gh-deploy --force