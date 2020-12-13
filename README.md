# Secret Santa


## Getting started

Run the script with using Python.

### Usage

```
python santa --names Hansel Gretel Woodcutter
```
Will print pairs of names from the list `[Hansel, Gretel, Woodcutter]`.

## Advanced options

The script includes a number of more advanced options for 
* outputting to directory/files
* custom URL-safe names


### Output to directory/files

By using the optional argument `--group [GROUP_NAME]`, the assignments will be output to a subsirectory instead of the console. 
```
python santa 
    --names Hansel Gretel Woodcutter 
    --group Breadcrumbs
```

### Custom URL-safe names

Not all characters can be represented tidily in URLs and file names. The script will automatically perform percent encoding such that `é` will be encoded to `%C3%A9`. If this is not desired, or names contain characters that cannot be encoded in this way, custom URL-safe names can be used.
```
python santa 
    --names     Hansel Grétel Woodcutter 
    --name-urls hansel gretel woodcutter 
```
And similarly for the group name:
```
python santa 
    --names     Hansel Gretel Woodcutter 
    --group     Breadcrumbs
    --group-url bread
```

### Fuzzy URLS

If files are publically accessible, it may be desirable to add some fuzz to filenames/URLs such that they cannot be guessed. For example, the URL `/hansel-4hjkl38shovd5i` is far harder to find that `/hansel`, preserving the spirit of *secret* santa.

Use the optional `--fuzz` argument to speficy the number of pseudo-random base-62 characters to generate.
```
python santa 
    --names Hansel Gretel Woodcutter 
    --group Breadcrumbs
    --fuzz  20
```

## License

This project is licensed under the MIT licence.