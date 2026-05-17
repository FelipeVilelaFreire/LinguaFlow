import type { NextConfig } from "next";
import path from "node:path";

const nextConfig: NextConfig = {
  transpilePackages: ["@linguaflow/shared-core"],
  webpack: (config) => {
    config.resolve.alias["@linguaflow/shared-core"] = path.resolve(__dirname, "../packages/shared-core/src/index.ts");
    return config;
  },
};

export default nextConfig;
